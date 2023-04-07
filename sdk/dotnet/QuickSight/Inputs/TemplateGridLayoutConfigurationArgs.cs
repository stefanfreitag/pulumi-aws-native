// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateGridLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("canvasSizeOptions")]
        public Input<Inputs.TemplateGridLayoutCanvasSizeOptionsArgs>? CanvasSizeOptions { get; set; }

        [Input("elements", required: true)]
        private InputList<Inputs.TemplateGridLayoutElementArgs>? _elements;
        public InputList<Inputs.TemplateGridLayoutElementArgs> Elements
        {
            get => _elements ?? (_elements = new InputList<Inputs.TemplateGridLayoutElementArgs>());
            set => _elements = value;
        }

        public TemplateGridLayoutConfigurationArgs()
        {
        }
        public static new TemplateGridLayoutConfigurationArgs Empty => new TemplateGridLayoutConfigurationArgs();
    }
}
