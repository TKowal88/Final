#include "helpers.h"
#include <math.h>
#include <stdio.h>

int limit(int a);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int grayavg;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            grayavg = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = grayavg;
            image[i][j].rgbtGreen = grayavg;
            image[i][j].rgbtRed = grayavg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE swap;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap = image[i][width - 1 - j];
            image[i][width - 1 - j] = image[i][j];
            image[i][j] = swap;

        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Copies the image into a 2D array buffer
    RGBTRIPLE buffer[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            buffer[i][j] = image[i][j];
        }
    }
// Calculates the average for each 3x3 box surrounding a pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalBlue = 0;
            int totalGreen = 0;
            int totalRed = 0;
            float pixelcount = 0.0;
            for (int k = - 1; k < 2; k++)
            {
                for (int l = - 1; l < 2; l++)
                {
                    if (i + k >= 0 && j + l >= 0 && i + k < height && j + l < width)
                    {
                        totalBlue += buffer[i + k][j + l].rgbtBlue;
                        totalGreen += buffer[i + k][j + l].rgbtGreen;
                        totalRed += buffer[i + k][j + l].rgbtRed;
                        pixelcount++;
                    }
                }
            }

// Passes the average into the original image array
            image[i][j].rgbtBlue = round(totalBlue / pixelcount);
            image[i][j].rgbtGreen = round(totalGreen / pixelcount);
            image[i][j].rgbtRed = round(totalRed / pixelcount);
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])

{
// Establishes two 3x3 arrays with the values to multiply pixels by
    int x[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int y[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Copies the image into a 2D array buffer
    RGBTRIPLE buffer[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            buffer[i][j] = image[i][j];
        }
    }
    int GxTotalBlue;
    int GxTotalGreen;
    int GxTotalRed;
    int GyTotalBlue;
    int GyTotalGreen;
    int GyTotalRed;
// Iterates through the image and multiplies each surrounding pixel by both of the 2D arrays
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            GxTotalBlue = 0;
            GxTotalGreen = 0;
            GxTotalRed = 0;
            GyTotalBlue = 0;
            GyTotalGreen = 0;
            GyTotalRed = 0;
            
// Calculates the new pixel values based on multiplication of pixels by the values in 2D arrays
            for (int k = - 1; k < 2; k++)
            {
                for (int l = - 1; l < 2; l++)
                {
                    if (i + k >= 0 && j + l >= 0 && i + k < height && j + l < width)
                    {
                        GxTotalBlue += buffer[i + k][j + l].rgbtBlue * x[k + 1][l + 1];
                        GxTotalGreen += buffer[i + k][j + l].rgbtGreen * x[k + 1][l + 1];
                        GxTotalRed += buffer[i + k][j + l].rgbtRed * x[k + 1][l + 1];
                        GyTotalBlue += buffer[i + k][j + l].rgbtBlue * y[k + 1][l + 1];
                        GyTotalGreen += buffer[i + k][j + l].rgbtGreen * y[k + 1][l + 1];
                        GyTotalRed +=  buffer[i + k][j + l].rgbtRed * y[k + 1][l + 1];
                    }
                }
            }
// Calculates the new pixel totals using the Sobel filter
            image[i][j].rgbtBlue = limit(round(sqrt(pow(GyTotalBlue, 2) + pow(GxTotalBlue, 2))));
            image[i][j].rgbtGreen = limit(round(sqrt(pow(GyTotalGreen, 2) + pow(GxTotalGreen, 2))));
            image[i][j].rgbtRed = limit(round(sqrt(pow(GyTotalRed, 2) + pow(GxTotalRed, 2))));
        }
    }
    return;
}
// Function limits the value of the pixel output to 255
int limit(int a)
{
    if (a > 255)
    {
        return 255;
    }

    else
    {
        return a;
    }
}