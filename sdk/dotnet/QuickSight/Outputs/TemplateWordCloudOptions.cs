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
    public sealed class TemplateWordCloudOptions
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateWordCloudCloudLayout? CloudLayout;
        public readonly double? MaximumStringLength;
        public readonly Pulumi.AwsNative.QuickSight.TemplateWordCloudWordCasing? WordCasing;
        public readonly Pulumi.AwsNative.QuickSight.TemplateWordCloudWordOrientation? WordOrientation;
        public readonly Pulumi.AwsNative.QuickSight.TemplateWordCloudWordPadding? WordPadding;
        public readonly Pulumi.AwsNative.QuickSight.TemplateWordCloudWordScaling? WordScaling;

        [OutputConstructor]
        private TemplateWordCloudOptions(
            Pulumi.AwsNative.QuickSight.TemplateWordCloudCloudLayout? cloudLayout,

            double? maximumStringLength,

            Pulumi.AwsNative.QuickSight.TemplateWordCloudWordCasing? wordCasing,

            Pulumi.AwsNative.QuickSight.TemplateWordCloudWordOrientation? wordOrientation,

            Pulumi.AwsNative.QuickSight.TemplateWordCloudWordPadding? wordPadding,

            Pulumi.AwsNative.QuickSight.TemplateWordCloudWordScaling? wordScaling)
        {
            CloudLayout = cloudLayout;
            MaximumStringLength = maximumStringLength;
            WordCasing = wordCasing;
            WordOrientation = wordOrientation;
            WordPadding = wordPadding;
            WordScaling = wordScaling;
        }
    }
}
