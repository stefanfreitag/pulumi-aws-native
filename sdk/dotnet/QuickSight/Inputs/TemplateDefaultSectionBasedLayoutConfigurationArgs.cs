// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateDefaultSectionBasedLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("canvasSizeOptions", required: true)]
        public Input<Inputs.TemplateSectionBasedLayoutCanvasSizeOptionsArgs> CanvasSizeOptions { get; set; } = null!;

        public TemplateDefaultSectionBasedLayoutConfigurationArgs()
        {
        }
        public static new TemplateDefaultSectionBasedLayoutConfigurationArgs Empty => new TemplateDefaultSectionBasedLayoutConfigurationArgs();
    }
}
