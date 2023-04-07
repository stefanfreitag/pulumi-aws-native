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
    public sealed class TemplateReferenceLineDataConfiguration
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateAxisBinding? AxisBinding;
        public readonly Outputs.TemplateReferenceLineDynamicDataConfiguration? DynamicConfiguration;
        public readonly Outputs.TemplateReferenceLineStaticDataConfiguration? StaticConfiguration;

        [OutputConstructor]
        private TemplateReferenceLineDataConfiguration(
            Pulumi.AwsNative.QuickSight.TemplateAxisBinding? axisBinding,

            Outputs.TemplateReferenceLineDynamicDataConfiguration? dynamicConfiguration,

            Outputs.TemplateReferenceLineStaticDataConfiguration? staticConfiguration)
        {
            AxisBinding = axisBinding;
            DynamicConfiguration = dynamicConfiguration;
            StaticConfiguration = staticConfiguration;
        }
    }
}
