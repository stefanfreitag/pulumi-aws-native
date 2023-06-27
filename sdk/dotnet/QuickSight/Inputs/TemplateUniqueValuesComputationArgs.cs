// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateUniqueValuesComputationArgs : global::Pulumi.ResourceArgs
    {
        [Input("category", required: true)]
        public Input<Inputs.TemplateDimensionFieldArgs> Category { get; set; } = null!;

        [Input("computationId", required: true)]
        public Input<string> ComputationId { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        public TemplateUniqueValuesComputationArgs()
        {
        }
        public static new TemplateUniqueValuesComputationArgs Empty => new TemplateUniqueValuesComputationArgs();
    }
}
