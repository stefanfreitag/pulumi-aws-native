// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateFilterOperationTargetVisualsConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("sameSheetTargetVisualConfiguration")]
        public Input<Inputs.TemplateSameSheetTargetVisualConfigurationArgs>? SameSheetTargetVisualConfiguration { get; set; }

        public TemplateFilterOperationTargetVisualsConfigurationArgs()
        {
        }
        public static new TemplateFilterOperationTargetVisualsConfigurationArgs Empty => new TemplateFilterOperationTargetVisualsConfigurationArgs();
    }
}
