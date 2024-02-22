// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Scheduler
{
    /// <summary>
    /// Definition of AWS::Scheduler::ScheduleGroup Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:scheduler:ScheduleGroup")]
    public partial class ScheduleGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the schedule group.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The time at which the schedule group was created.
        /// </summary>
        [Output("creationDate")]
        public Output<string> CreationDate { get; private set; } = null!;

        /// <summary>
        /// The time at which the schedule group was last modified.
        /// </summary>
        [Output("lastModificationDate")]
        public Output<string> LastModificationDate { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("state")]
        public Output<Pulumi.AwsNative.Scheduler.ScheduleGroupState> State { get; private set; } = null!;

        /// <summary>
        /// The list of tags to associate with the schedule group.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ScheduleGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScheduleGroup(string name, ScheduleGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:scheduler:ScheduleGroup", name, args ?? new ScheduleGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ScheduleGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:scheduler:ScheduleGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ScheduleGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScheduleGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ScheduleGroup(name, id, options);
        }
    }

    public sealed class ScheduleGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The list of tags to associate with the schedule group.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ScheduleGroupArgs()
        {
        }
        public static new ScheduleGroupArgs Empty => new ScheduleGroupArgs();
    }
}
