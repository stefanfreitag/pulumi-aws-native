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
    public sealed class DashboardFilterTextAreaControl
    {
        public readonly string? Delimiter;
        public readonly Outputs.DashboardTextAreaControlDisplayOptions? DisplayOptions;
        public readonly string FilterControlId;
        public readonly string SourceFilterId;
        public readonly string Title;

        [OutputConstructor]
        private DashboardFilterTextAreaControl(
            string? delimiter,

            Outputs.DashboardTextAreaControlDisplayOptions? displayOptions,

            string filterControlId,

            string sourceFilterId,

            string title)
        {
            Delimiter = delimiter;
            DisplayOptions = displayOptions;
            FilterControlId = filterControlId;
            SourceFilterId = sourceFilterId;
            Title = title;
        }
    }
}
