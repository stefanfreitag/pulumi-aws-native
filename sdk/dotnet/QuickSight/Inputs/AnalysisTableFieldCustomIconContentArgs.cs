// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTableFieldCustomIconContentArgs : global::Pulumi.ResourceArgs
    {
        [Input("icon")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTableFieldIconSetType>? Icon { get; set; }

        public AnalysisTableFieldCustomIconContentArgs()
        {
        }
        public static new AnalysisTableFieldCustomIconContentArgs Empty => new AnalysisTableFieldCustomIconContentArgs();
    }
}
