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
    public sealed class DashboardCustomContentConfiguration
    {
        public readonly Pulumi.AwsNative.QuickSight.DashboardCustomContentType? ContentType;
        public readonly string? ContentUrl;
        public readonly Pulumi.AwsNative.QuickSight.DashboardCustomContentImageScalingConfiguration? ImageScaling;

        [OutputConstructor]
        private DashboardCustomContentConfiguration(
            Pulumi.AwsNative.QuickSight.DashboardCustomContentType? contentType,

            string? contentUrl,

            Pulumi.AwsNative.QuickSight.DashboardCustomContentImageScalingConfiguration? imageScaling)
        {
            ContentType = contentType;
            ContentUrl = contentUrl;
            ImageScaling = imageScaling;
        }
    }
}
