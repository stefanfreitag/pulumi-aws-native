// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTableCellConditionalFormattingArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        [Input("textFormat")]
        public Input<Inputs.TemplateTextConditionalFormatArgs>? TextFormat { get; set; }

        public TemplateTableCellConditionalFormattingArgs()
        {
        }
        public static new TemplateTableCellConditionalFormattingArgs Empty => new TemplateTableCellConditionalFormattingArgs();
    }
}
