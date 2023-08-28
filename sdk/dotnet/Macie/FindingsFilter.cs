// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Macie
{
    /// <summary>
    /// Macie FindingsFilter resource schema.
    /// </summary>
    [AwsNativeResourceType("aws-native:macie:FindingsFilter")]
    public partial class FindingsFilter : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Findings filter action.
        /// </summary>
        [Output("action")]
        public Output<Pulumi.AwsNative.Macie.FindingsFilterFindingFilterAction?> Action { get; private set; } = null!;

        /// <summary>
        /// Findings filter ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Findings filter description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Findings filter criteria.
        /// </summary>
        [Output("findingCriteria")]
        public Output<Outputs.FindingsFilterFindingCriteria> FindingCriteria { get; private set; } = null!;

        /// <summary>
        /// Findings filter name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Findings filter position.
        /// </summary>
        [Output("position")]
        public Output<int?> Position { get; private set; } = null!;

        /// <summary>
        /// A collection of tags associated with a resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.FindingsFilterTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FindingsFilter resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FindingsFilter(string name, FindingsFilterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:macie:FindingsFilter", name, args ?? new FindingsFilterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FindingsFilter(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:macie:FindingsFilter", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing FindingsFilter resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FindingsFilter Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FindingsFilter(name, id, options);
        }
    }

    public sealed class FindingsFilterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Findings filter action.
        /// </summary>
        [Input("action")]
        public Input<Pulumi.AwsNative.Macie.FindingsFilterFindingFilterAction>? Action { get; set; }

        /// <summary>
        /// Findings filter description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Findings filter criteria.
        /// </summary>
        [Input("findingCriteria", required: true)]
        public Input<Inputs.FindingsFilterFindingCriteriaArgs> FindingCriteria { get; set; } = null!;

        /// <summary>
        /// Findings filter name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Findings filter position.
        /// </summary>
        [Input("position")]
        public Input<int>? Position { get; set; }

        [Input("tags")]
        private InputList<Inputs.FindingsFilterTagArgs>? _tags;

        /// <summary>
        /// A collection of tags associated with a resource
        /// </summary>
        public InputList<Inputs.FindingsFilterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FindingsFilterTagArgs>());
            set => _tags = value;
        }

        public FindingsFilterArgs()
        {
        }
        public static new FindingsFilterArgs Empty => new FindingsFilterArgs();
    }
}
