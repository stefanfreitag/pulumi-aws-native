// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently
{
    /// <summary>
    /// Resource Type definition for AWS::Evidently::Launch.
    /// </summary>
    [AwsNativeResourceType("aws-native:evidently:Launch")]
    public partial class Launch : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Start or Stop Launch Launch. Default is not started.
        /// </summary>
        [Output("executionStatus")]
        public Output<Outputs.LaunchExecutionStatusObject?> ExecutionStatus { get; private set; } = null!;

        [Output("groups")]
        public Output<ImmutableArray<Outputs.LaunchGroupObject>> Groups { get; private set; } = null!;

        [Output("metricMonitors")]
        public Output<ImmutableArray<Outputs.LaunchMetricDefinitionObject>> MetricMonitors { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        [Output("randomizationSalt")]
        public Output<string?> RandomizationSalt { get; private set; } = null!;

        [Output("scheduledSplitsConfig")]
        public Output<ImmutableArray<Outputs.LaunchStepConfig>> ScheduledSplitsConfig { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Launch resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Launch(string name, LaunchArgs args, CustomResourceOptions? options = null)
            : base("aws-native:evidently:Launch", name, args ?? new LaunchArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Launch(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:evidently:Launch", name, null, MakeResourceOptions(options, id))
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
                    "project",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Launch resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Launch Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Launch(name, id, options);
        }
    }

    public sealed class LaunchArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Start or Stop Launch Launch. Default is not started.
        /// </summary>
        [Input("executionStatus")]
        public Input<Inputs.LaunchExecutionStatusObjectArgs>? ExecutionStatus { get; set; }

        [Input("groups", required: true)]
        private InputList<Inputs.LaunchGroupObjectArgs>? _groups;
        public InputList<Inputs.LaunchGroupObjectArgs> Groups
        {
            get => _groups ?? (_groups = new InputList<Inputs.LaunchGroupObjectArgs>());
            set => _groups = value;
        }

        [Input("metricMonitors")]
        private InputList<Inputs.LaunchMetricDefinitionObjectArgs>? _metricMonitors;
        public InputList<Inputs.LaunchMetricDefinitionObjectArgs> MetricMonitors
        {
            get => _metricMonitors ?? (_metricMonitors = new InputList<Inputs.LaunchMetricDefinitionObjectArgs>());
            set => _metricMonitors = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        [Input("randomizationSalt")]
        public Input<string>? RandomizationSalt { get; set; }

        [Input("scheduledSplitsConfig", required: true)]
        private InputList<Inputs.LaunchStepConfigArgs>? _scheduledSplitsConfig;
        public InputList<Inputs.LaunchStepConfigArgs> ScheduledSplitsConfig
        {
            get => _scheduledSplitsConfig ?? (_scheduledSplitsConfig = new InputList<Inputs.LaunchStepConfigArgs>());
            set => _scheduledSplitsConfig = value;
        }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public LaunchArgs()
        {
        }
        public static new LaunchArgs Empty => new LaunchArgs();
    }
}
