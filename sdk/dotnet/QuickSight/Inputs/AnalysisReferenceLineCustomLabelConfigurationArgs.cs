// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisReferenceLineCustomLabelConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLabel", required: true)]
        public Input<string> CustomLabel { get; set; } = null!;

        public AnalysisReferenceLineCustomLabelConfigurationArgs()
        {
        }
        public static new AnalysisReferenceLineCustomLabelConfigurationArgs Empty => new AnalysisReferenceLineCustomLabelConfigurationArgs();
    }
}
