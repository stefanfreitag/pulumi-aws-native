// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisDateAxisOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("missingDateVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? MissingDateVisibility { get; set; }

        public AnalysisDateAxisOptionsArgs()
        {
        }
        public static new AnalysisDateAxisOptionsArgs Empty => new AnalysisDateAxisOptionsArgs();
    }
}
