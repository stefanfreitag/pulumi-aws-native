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
    public sealed class DashboardTableFieldCustomTextContent
    {
        public readonly Outputs.DashboardFontConfiguration FontConfiguration;
        public readonly string? Value;

        [OutputConstructor]
        private DashboardTableFieldCustomTextContent(
            Outputs.DashboardFontConfiguration fontConfiguration,

            string? value)
        {
            FontConfiguration = fontConfiguration;
            Value = value;
        }
    }
}
