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
    public sealed class TemplateTableFieldURLConfiguration
    {
        public readonly Outputs.TemplateTableFieldImageConfiguration? ImageConfiguration;
        public readonly Outputs.TemplateTableFieldLinkConfiguration? LinkConfiguration;

        [OutputConstructor]
        private TemplateTableFieldURLConfiguration(
            Outputs.TemplateTableFieldImageConfiguration? imageConfiguration,

            Outputs.TemplateTableFieldLinkConfiguration? linkConfiguration)
        {
            ImageConfiguration = imageConfiguration;
            LinkConfiguration = linkConfiguration;
        }
    }
}
