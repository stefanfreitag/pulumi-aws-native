// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateConditionalFormattingCustomIconOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("icon")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateIcon>? Icon { get; set; }

        [Input("unicodeIcon")]
        public Input<string>? UnicodeIcon { get; set; }

        public TemplateConditionalFormattingCustomIconOptionsArgs()
        {
        }
        public static new TemplateConditionalFormattingCustomIconOptionsArgs Empty => new TemplateConditionalFormattingCustomIconOptionsArgs();
    }
}
