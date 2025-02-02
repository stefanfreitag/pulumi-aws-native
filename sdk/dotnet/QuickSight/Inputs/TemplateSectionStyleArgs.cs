// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateSectionStyleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("height")]
        public Input<string>? Height { get; set; }

        [Input("padding")]
        public Input<Inputs.TemplateSpacingArgs>? Padding { get; set; }

        public TemplateSectionStyleArgs()
        {
        }
        public static new TemplateSectionStyleArgs Empty => new TemplateSectionStyleArgs();
    }
}
