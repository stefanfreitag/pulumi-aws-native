// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling.Inputs
{

    public sealed class AutoScalingGroupNotificationConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("notificationTypes")]
        private InputList<string>? _notificationTypes;
        public InputList<string> NotificationTypes
        {
            get => _notificationTypes ?? (_notificationTypes = new InputList<string>());
            set => _notificationTypes = value;
        }

        [Input("topicARN", required: true)]
        public Input<string> TopicARN { get; set; } = null!;

        public AutoScalingGroupNotificationConfigurationArgs()
        {
        }
        public static new AutoScalingGroupNotificationConfigurationArgs Empty => new AutoScalingGroupNotificationConfigurationArgs();
    }
}
