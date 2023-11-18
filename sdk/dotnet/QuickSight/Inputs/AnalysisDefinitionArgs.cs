// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisDefinitionArgs : global::Pulumi.ResourceArgs
    {
        [Input("analysisDefaults")]
        public Input<Inputs.AnalysisDefaultsArgs>? AnalysisDefaults { get; set; }

        [Input("calculatedFields")]
        private InputList<Inputs.AnalysisCalculatedFieldArgs>? _calculatedFields;
        public InputList<Inputs.AnalysisCalculatedFieldArgs> CalculatedFields
        {
            get => _calculatedFields ?? (_calculatedFields = new InputList<Inputs.AnalysisCalculatedFieldArgs>());
            set => _calculatedFields = value;
        }

        [Input("columnConfigurations")]
        private InputList<Inputs.AnalysisColumnConfigurationArgs>? _columnConfigurations;
        public InputList<Inputs.AnalysisColumnConfigurationArgs> ColumnConfigurations
        {
            get => _columnConfigurations ?? (_columnConfigurations = new InputList<Inputs.AnalysisColumnConfigurationArgs>());
            set => _columnConfigurations = value;
        }

        [Input("dataSetIdentifierDeclarations", required: true)]
        private InputList<Inputs.AnalysisDataSetIdentifierDeclarationArgs>? _dataSetIdentifierDeclarations;
        public InputList<Inputs.AnalysisDataSetIdentifierDeclarationArgs> DataSetIdentifierDeclarations
        {
            get => _dataSetIdentifierDeclarations ?? (_dataSetIdentifierDeclarations = new InputList<Inputs.AnalysisDataSetIdentifierDeclarationArgs>());
            set => _dataSetIdentifierDeclarations = value;
        }

        [Input("filterGroups")]
        private InputList<Inputs.AnalysisFilterGroupArgs>? _filterGroups;
        public InputList<Inputs.AnalysisFilterGroupArgs> FilterGroups
        {
            get => _filterGroups ?? (_filterGroups = new InputList<Inputs.AnalysisFilterGroupArgs>());
            set => _filterGroups = value;
        }

        [Input("options")]
        public Input<Inputs.AnalysisAssetOptionsArgs>? Options { get; set; }

        [Input("parameterDeclarations")]
        private InputList<Inputs.AnalysisParameterDeclarationArgs>? _parameterDeclarations;
        public InputList<Inputs.AnalysisParameterDeclarationArgs> ParameterDeclarations
        {
            get => _parameterDeclarations ?? (_parameterDeclarations = new InputList<Inputs.AnalysisParameterDeclarationArgs>());
            set => _parameterDeclarations = value;
        }

        [Input("sheets")]
        private InputList<Inputs.AnalysisSheetDefinitionArgs>? _sheets;
        public InputList<Inputs.AnalysisSheetDefinitionArgs> Sheets
        {
            get => _sheets ?? (_sheets = new InputList<Inputs.AnalysisSheetDefinitionArgs>());
            set => _sheets = value;
        }

        public AnalysisDefinitionArgs()
        {
        }
        public static new AnalysisDefinitionArgs Empty => new AnalysisDefinitionArgs();
    }
}
