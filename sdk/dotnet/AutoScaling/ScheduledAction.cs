// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling
{
    /// <summary>
    /// Resource Type definition for AWS::AutoScaling::ScheduledAction
    /// </summary>
    [Obsolete(@"ScheduledAction is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:autoscaling:ScheduledAction")]
    public partial class ScheduledAction : global::Pulumi.CustomResource
    {
        [Output("autoScalingGroupName")]
        public Output<string> AutoScalingGroupName { get; private set; } = null!;

        [Output("desiredCapacity")]
        public Output<int?> DesiredCapacity { get; private set; } = null!;

        [Output("endTime")]
        public Output<string?> EndTime { get; private set; } = null!;

        [Output("maxSize")]
        public Output<int?> MaxSize { get; private set; } = null!;

        [Output("minSize")]
        public Output<int?> MinSize { get; private set; } = null!;

        [Output("recurrence")]
        public Output<string?> Recurrence { get; private set; } = null!;

        [Output("startTime")]
        public Output<string?> StartTime { get; private set; } = null!;

        [Output("timeZone")]
        public Output<string?> TimeZone { get; private set; } = null!;


        /// <summary>
        /// Create a ScheduledAction resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScheduledAction(string name, ScheduledActionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:autoscaling:ScheduledAction", name, args ?? new ScheduledActionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ScheduledAction(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:autoscaling:ScheduledAction", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ScheduledAction resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScheduledAction Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ScheduledAction(name, id, options);
        }
    }

    public sealed class ScheduledActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoScalingGroupName", required: true)]
        public Input<string> AutoScalingGroupName { get; set; } = null!;

        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        [Input("minSize")]
        public Input<int>? MinSize { get; set; }

        [Input("recurrence")]
        public Input<string>? Recurrence { get; set; }

        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        [Input("timeZone")]
        public Input<string>? TimeZone { get; set; }

        public ScheduledActionArgs()
        {
        }
        public static new ScheduledActionArgs Empty => new ScheduledActionArgs();
    }
}
