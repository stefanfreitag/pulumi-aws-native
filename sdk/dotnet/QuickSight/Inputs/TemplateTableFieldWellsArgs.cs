// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTableFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("tableAggregatedFieldWells")]
        public Input<Inputs.TemplateTableAggregatedFieldWellsArgs>? TableAggregatedFieldWells { get; set; }

        [Input("tableUnaggregatedFieldWells")]
        public Input<Inputs.TemplateTableUnaggregatedFieldWellsArgs>? TableUnaggregatedFieldWells { get; set; }

        public TemplateTableFieldWellsArgs()
        {
        }
        public static new TemplateTableFieldWellsArgs Empty => new TemplateTableFieldWellsArgs();
    }
}
