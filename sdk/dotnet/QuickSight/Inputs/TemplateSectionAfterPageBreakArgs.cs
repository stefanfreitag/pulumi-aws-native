// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateSectionAfterPageBreakArgs : global::Pulumi.ResourceArgs
    {
        [Input("status")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateSectionPageBreakStatus>? Status { get; set; }

        public TemplateSectionAfterPageBreakArgs()
        {
        }
        public static new TemplateSectionAfterPageBreakArgs Empty => new TemplateSectionAfterPageBreakArgs();
    }
}
