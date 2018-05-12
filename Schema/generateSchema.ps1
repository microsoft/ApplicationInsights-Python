$generatorPath = "C:\src\mseng\AppInsights-Common"
$publicSchemaLocation = "https://raw.githubusercontent.com/Microsoft/ApplicationInsights-Home/master/EndpointSpecs/Schemas/Bond"
$currentDir = $scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
$schemasPath = "$currentDir\PublicSchema"

#fix path
$generatorPath = "$generatorPath\..\bin\Debug\BondSchemaGenerator\BondSchemaGenerator"


#####################################################################
## PUBLIC SCHEMA
#####################################################################
mkdir -Force $schemasPath

function RegExReplace([string]$fileName, [string]$regex, [string]$replacement="")
{
    $content = Get-Content $fileName 
    $content = $content -creplace $regex,$replacement 
    $content | Set-Content $fileName
}

# Download public schema from the github
@(
"AvailabilityData.bond",
"Base.bond",
"ContextTagKeys.bond",
"Data.bond", 
"DataPoint.bond", 
"DataPointType.bond", 
"Domain.bond", 
"Envelope.bond", 
"EventData.bond", 
"ExceptionData.bond", 
"ExceptionDetails.bond", 
"MessageData.bond", 
"MetricData.bond", 
"PageViewData.bond", 
"PageViewPerfData.bond", 
"RemoteDependencyData.bond", 
"RequestData.bond", 
"SeverityLevel.bond", 
"StackFrame.bond"
)  | ForEach-Object { 
    $fileName = $_
    & Invoke-WebRequest -o "$currentDir\PublicSchema\$fileName" "$publicSchemaLocation/$fileName"
    RegExReplace "$currentDir\PublicSchema\$fileName" "`n" "`r`n"
}

# Generate public schema using bond generator
& "$generatorPath\BondSchemaGenerator.exe" -v -i "$schemasPath\AvailabilityData.bond" -i "$schemasPath\Base.bond" -i "$schemasPath\ContextTagKeys.bond" -i "$schemasPath\Data.bond" -i "$schemasPath\DataPoint.bond" -i "$schemasPath\DataPointType.bond" -i "$schemasPath\Domain.bond" -i "$schemasPath\Envelope.bond" -i "$schemasPath\EventData.bond" -i "$schemasPath\ExceptionData.bond" -i "$schemasPath\ExceptionDetails.bond" -i "$schemasPath\MessageData.bond" -i "$schemasPath\MetricData.bond"  -i "$schemasPath\PageViewData.bond" -i "$schemasPath\PageViewPerfData.bond" -i "$schemasPath\RemoteDependencyData.bond" -i "$schemasPath\RequestData.bond" -i "$schemasPath\SeverityLevel.bond" -i "$schemasPath\StackFrame.bond" -o "$currentDir\..\" -e PythonProductLanguage -t PythonProductLayout 

