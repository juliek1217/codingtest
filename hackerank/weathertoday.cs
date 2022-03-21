// returns sunshine

using System;

namespace WeatherApplication
{
public
    class WeatherDefault // Base class (parent)
    {
    public
        virtual string GetWeather()
        {
            return GetWeatherToday();
        }
    public
        virtual string GetWeatherToday()
        {
            return "sunshine";
        }
    }

    public class WeatherToday : WeatherDefault // Derived class (child)
    {
    public
        virtual string GetWeatherToday()
        {
            return "snow";
        }
    }

    class Weather
    {
        static void Main(string[] args)
        {
            WeatherToday w = new WeatherToday();
            Console.WriteLine(w.GetWeather());
            Console.ReadKey();
        }
    }
}