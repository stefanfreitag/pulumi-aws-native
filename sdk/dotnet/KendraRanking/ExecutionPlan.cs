// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KendraRanking
{
    /// <summary>
    /// A KendraRanking Rescore execution plan
    /// </summary>
    [AwsNativeResourceType("aws-native:kendraranking:ExecutionPlan")]
    public partial class ExecutionPlan : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Capacity units
        /// </summary>
        [Output("capacityUnits")]
        public Output<Outputs.ExecutionPlanCapacityUnitsConfiguration?> CapacityUnits { get; private set; } = null!;

        /// <summary>
        /// A description for the execution plan
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Tags for labeling the execution plan
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ExecutionPlan resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ExecutionPlan(string name, ExecutionPlanArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:kendraranking:ExecutionPlan", name, args ?? new ExecutionPlanArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ExecutionPlan(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kendraranking:ExecutionPlan", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ExecutionPlan resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ExecutionPlan Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ExecutionPlan(name, id, options);
        }
    }

    public sealed class ExecutionPlanArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Capacity units
        /// </summary>
        [Input("capacityUnits")]
        public Input<Inputs.ExecutionPlanCapacityUnitsConfigurationArgs>? CapacityUnits { get; set; }

        /// <summary>
        /// A description for the execution plan
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// Tags for labeling the execution plan
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ExecutionPlanArgs()
        {
        }
        public static new ExecutionPlanArgs Empty => new ExecutionPlanArgs();
    }
}
