// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplatePivotTableConditionalFormattingScopeArgs : global::Pulumi.ResourceArgs
    {
        [Input("role")]
        public Input<Pulumi.AwsNative.QuickSight.TemplatePivotTableConditionalFormattingScopeRole>? Role { get; set; }

        public TemplatePivotTableConditionalFormattingScopeArgs()
        {
        }
        public static new TemplatePivotTableConditionalFormattingScopeArgs Empty => new TemplatePivotTableConditionalFormattingScopeArgs();
    }
}
