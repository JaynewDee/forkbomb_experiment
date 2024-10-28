# Use the .NET SDK image for building the application
FROM mcr.microsoft.com/dotnet/sdk:latest AS builder

# Set the working directory
WORKDIR /app

# Copy the C# source code into the builder container
COPY ForkBomb.csproj .
COPY ForkBomb.cs .

# Build the C# application without creating a new template
RUN dotnet restore ForkBomb.csproj 
RUN dotnet build ForkBomb.csproj -c Release -o out

# Use a runtime image to run the application
FROM mcr.microsoft.com/dotnet/runtime:latest

# Set the working directory
WORKDIR /app

# Copy the compiled application from the builder stage
COPY --from=builder /app/out .

# Run the compiled application
CMD ["dotnet", "ForkBomb.dll"]
