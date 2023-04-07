// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class AnalysisDefinition
    {
        public readonly Outputs.AnalysisDefaults? AnalysisDefaults;
        public readonly ImmutableArray<Outputs.AnalysisCalculatedField> CalculatedFields;
        public readonly ImmutableArray<Outputs.AnalysisColumnConfiguration> ColumnConfigurations;
        public readonly ImmutableArray<Outputs.AnalysisDataSetIdentifierDeclaration> DataSetIdentifierDeclarations;
        public readonly ImmutableArray<Outputs.AnalysisFilterGroup> FilterGroups;
        public readonly ImmutableArray<Outputs.AnalysisParameterDeclaration> ParameterDeclarations;
        public readonly ImmutableArray<Outputs.AnalysisSheetDefinition> Sheets;

        [OutputConstructor]
        private AnalysisDefinition(
            Outputs.AnalysisDefaults? analysisDefaults,

            ImmutableArray<Outputs.AnalysisCalculatedField> calculatedFields,

            ImmutableArray<Outputs.AnalysisColumnConfiguration> columnConfigurations,

            ImmutableArray<Outputs.AnalysisDataSetIdentifierDeclaration> dataSetIdentifierDeclarations,

            ImmutableArray<Outputs.AnalysisFilterGroup> filterGroups,

            ImmutableArray<Outputs.AnalysisParameterDeclaration> parameterDeclarations,

            ImmutableArray<Outputs.AnalysisSheetDefinition> sheets)
        {
            AnalysisDefaults = analysisDefaults;
            CalculatedFields = calculatedFields;
            ColumnConfigurations = columnConfigurations;
            DataSetIdentifierDeclarations = dataSetIdentifierDeclarations;
            FilterGroups = filterGroups;
            ParameterDeclarations = parameterDeclarations;
            Sheets = sheets;
        }
    }
}
