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
    /// The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.
    /// </summary>
    [AwsNativeResourceType("aws-native:autoscaling:ScheduledAction")]
    public partial class ScheduledAction : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Auto Scaling group.
        /// </summary>
        [Output("autoScalingGroupName")]
        public Output<string> AutoScalingGroupName { get; private set; } = null!;

        /// <summary>
        /// The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        /// </summary>
        [Output("desiredCapacity")]
        public Output<int?> DesiredCapacity { get; private set; } = null!;

        /// <summary>
        /// The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        /// </summary>
        [Output("endTime")]
        public Output<string?> EndTime { get; private set; } = null!;

        /// <summary>
        /// The minimum size of the Auto Scaling group.
        /// </summary>
        [Output("maxSize")]
        public Output<int?> MaxSize { get; private set; } = null!;

        /// <summary>
        /// The minimum size of the Auto Scaling group.
        /// </summary>
        [Output("minSize")]
        public Output<int?> MinSize { get; private set; } = null!;

        /// <summary>
        /// The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        /// </summary>
        [Output("recurrence")]
        public Output<string?> Recurrence { get; private set; } = null!;

        /// <summary>
        /// Auto-generated unique identifier
        /// </summary>
        [Output("scheduledActionName")]
        public Output<string> ScheduledActionName { get; private set; } = null!;

        /// <summary>
        /// The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        /// </summary>
        [Output("startTime")]
        public Output<string?> StartTime { get; private set; } = null!;

        /// <summary>
        /// The time zone for the cron expression.
        /// </summary>
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
        /// <summary>
        /// The name of the Auto Scaling group.
        /// </summary>
        [Input("autoScalingGroupName", required: true)]
        public Input<string> AutoScalingGroupName { get; set; } = null!;

        /// <summary>
        /// The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        /// </summary>
        [Input("desiredCapacity")]
        public Input<int>? DesiredCapacity { get; set; }

        /// <summary>
        /// The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The minimum size of the Auto Scaling group.
        /// </summary>
        [Input("maxSize")]
        public Input<int>? MaxSize { get; set; }

        /// <summary>
        /// The minimum size of the Auto Scaling group.
        /// </summary>
        [Input("minSize")]
        public Input<int>? MinSize { get; set; }

        /// <summary>
        /// The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        /// </summary>
        [Input("recurrence")]
        public Input<string>? Recurrence { get; set; }

        /// <summary>
        /// The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        /// <summary>
        /// The time zone for the cron expression.
        /// </summary>
        [Input("timeZone")]
        public Input<string>? TimeZone { get; set; }

        public ScheduledActionArgs()
        {
        }
        public static new ScheduledActionArgs Empty => new ScheduledActionArgs();
    }
}
