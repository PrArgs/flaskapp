# Function to automatically run Python files
function Invoke-PythonFile {
    param([string]$FileName)
    
    if ($FileName -like "*.py") {
        # Check if we're in a virtual environment
        if (Test-Path ".venv\Scripts\python.exe") {
            Write-Host "Running with virtual environment Python..." -ForegroundColor Green
            & ".venv\Scripts\python.exe" $FileName
        } else {
            Write-Host "Running with system Python..." -ForegroundColor Yellow
            & "python" $FileName
        }
    } else {
        Write-Host "Not a Python file: $FileName" -ForegroundColor Red
    }
}

# Alias to make it easier to use
Set-Alias -Name py -Value Invoke-PythonFile

# Advanced: Override the default behavior for .py files
function Invoke-Command {
    param(
        [Parameter(Mandatory=$true, Position=0)]
        [string]$Name,
        [Parameter(Position=1)]
        [object[]]$ArgumentList
    )
    
    # Check if it's a .py file in current directory
    if ($Name -like "*.py" -and (Test-Path $Name)) {
        Invoke-PythonFile $Name
    } else {
        # Use the original Invoke-Command for everything else
        & $Name @ArgumentList
    }
}

# Create a function that will be called for unknown commands
function Invoke-UnknownCommand {
    param([string]$CommandName)
    
    # Check if it's a .py file
    if ($CommandName -like "*.py" -and (Test-Path $CommandName)) {
        Invoke-PythonFile $CommandName
    } else {
        Write-Host "Command not found: $CommandName" -ForegroundColor Red
    }
} 