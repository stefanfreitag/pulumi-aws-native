// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisNumericRangeFilterValueArgs : global::Pulumi.ResourceArgs
    {
        [Input("parameter")]
        public Input<string>? Parameter { get; set; }

        [Input("staticValue")]
        public Input<double>? StaticValue { get; set; }

        public AnalysisNumericRangeFilterValueArgs()
        {
        }
        public static new AnalysisNumericRangeFilterValueArgs Empty => new AnalysisNumericRangeFilterValueArgs();
    }
}
