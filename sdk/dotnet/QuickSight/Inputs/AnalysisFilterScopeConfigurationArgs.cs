// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFilterScopeConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("selectedSheets")]
        public Input<Inputs.AnalysisSelectedSheetsFilterScopeConfigurationArgs>? SelectedSheets { get; set; }

        public AnalysisFilterScopeConfigurationArgs()
        {
        }
        public static new AnalysisFilterScopeConfigurationArgs Empty => new AnalysisFilterScopeConfigurationArgs();
    }
}
