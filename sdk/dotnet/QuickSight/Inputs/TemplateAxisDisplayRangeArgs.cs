// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateAxisDisplayRangeArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataDriven")]
        public Input<Inputs.TemplateAxisDisplayDataDrivenRangeArgs>? DataDriven { get; set; }

        [Input("minMax")]
        public Input<Inputs.TemplateAxisDisplayMinMaxRangeArgs>? MinMax { get; set; }

        public TemplateAxisDisplayRangeArgs()
        {
        }
        public static new TemplateAxisDisplayRangeArgs Empty => new TemplateAxisDisplayRangeArgs();
    }
}
