// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena
{
    /// <summary>
    /// Resource schema for AWS::Athena::WorkGroup
    /// </summary>
    [AwsNativeResourceType("aws-native:athena:WorkGroup")]
    public partial class WorkGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The date and time the workgroup was created.
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        /// <summary>
        /// The workgroup description.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The workGroup name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        /// </summary>
        [Output("recursiveDeleteOption")]
        public Output<bool?> RecursiveDeleteOption { get; private set; } = null!;

        /// <summary>
        /// The state of the workgroup: ENABLED or DISABLED.
        /// </summary>
        [Output("state")]
        public Output<Pulumi.AwsNative.Athena.WorkGroupState?> State { get; private set; } = null!;

        /// <summary>
        /// One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The workgroup configuration
        /// </summary>
        [Output("workGroupConfiguration")]
        public Output<Outputs.WorkGroupConfiguration?> WorkGroupConfiguration { get; private set; } = null!;

        /// <summary>
        /// The workgroup configuration update object
        /// </summary>
        [Output("workGroupConfigurationUpdates")]
        public Output<Outputs.WorkGroupConfigurationUpdates?> WorkGroupConfigurationUpdates { get; private set; } = null!;


        /// <summary>
        /// Create a WorkGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WorkGroup(string name, WorkGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:athena:WorkGroup", name, args ?? new WorkGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WorkGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:athena:WorkGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing WorkGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WorkGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new WorkGroup(name, id, options);
        }
    }

    public sealed class WorkGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The workgroup description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The workGroup name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        /// </summary>
        [Input("recursiveDeleteOption")]
        public Input<bool>? RecursiveDeleteOption { get; set; }

        /// <summary>
        /// The state of the workgroup: ENABLED or DISABLED.
        /// </summary>
        [Input("state")]
        public Input<Pulumi.AwsNative.Athena.WorkGroupState>? State { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The workgroup configuration
        /// </summary>
        [Input("workGroupConfiguration")]
        public Input<Inputs.WorkGroupConfigurationArgs>? WorkGroupConfiguration { get; set; }

        /// <summary>
        /// The workgroup configuration update object
        /// </summary>
        [Input("workGroupConfigurationUpdates")]
        public Input<Inputs.WorkGroupConfigurationUpdatesArgs>? WorkGroupConfigurationUpdates { get; set; }

        public WorkGroupArgs()
        {
        }
        public static new WorkGroupArgs Empty => new WorkGroupArgs();
    }
}
