// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplatePivotTableFieldOption
    {
        public readonly string? CustomLabel;
        public readonly string FieldId;
        public readonly Pulumi.AwsNative.QuickSight.TemplateVisibility? Visibility;

        [OutputConstructor]
        private TemplatePivotTableFieldOption(
            string? customLabel,

            string fieldId,

            Pulumi.AwsNative.QuickSight.TemplateVisibility? visibility)
        {
            CustomLabel = customLabel;
            FieldId = fieldId;
            Visibility = visibility;
        }
    }
}
