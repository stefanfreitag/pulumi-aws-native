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
    public sealed class TemplateGlobalTableBorderOptions
    {
        public readonly Outputs.TemplateTableSideBorderOptions? SideSpecificBorder;
        public readonly Outputs.TemplateTableBorderOptions? UniformBorder;

        [OutputConstructor]
        private TemplateGlobalTableBorderOptions(
            Outputs.TemplateTableSideBorderOptions? sideSpecificBorder,

            Outputs.TemplateTableBorderOptions? uniformBorder)
        {
            SideSpecificBorder = sideSpecificBorder;
            UniformBorder = uniformBorder;
        }
    }
}
