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
    public sealed class TemplateCategoryDrillDownFilter
    {
        public readonly ImmutableArray<string> CategoryValues;
        public readonly Outputs.TemplateColumnIdentifier Column;

        [OutputConstructor]
        private TemplateCategoryDrillDownFilter(
            ImmutableArray<string> categoryValues,

            Outputs.TemplateColumnIdentifier column)
        {
            CategoryValues = categoryValues;
            Column = column;
        }
    }
}
