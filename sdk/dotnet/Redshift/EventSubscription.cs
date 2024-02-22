// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    /// <summary>
    /// The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
    /// </summary>
    [AwsNativeResourceType("aws-native:redshift:EventSubscription")]
    public partial class EventSubscription : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Amazon Redshift event notification subscription.
        /// </summary>
        [Output("custSubscriptionId")]
        public Output<string> CustSubscriptionId { get; private set; } = null!;

        /// <summary>
        /// The AWS account associated with the Amazon Redshift event notification subscription.
        /// </summary>
        [Output("customerAwsId")]
        public Output<string> CustomerAwsId { get; private set; } = null!;

        /// <summary>
        /// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        /// </summary>
        [Output("eventCategories")]
        public Output<ImmutableArray<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem>> EventCategories { get; private set; } = null!;

        /// <summary>
        /// The list of Amazon Redshift event categories specified in the event notification subscription.
        /// </summary>
        [Output("eventCategoriesList")]
        public Output<ImmutableArray<string>> EventCategoriesList { get; private set; } = null!;

        /// <summary>
        /// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        /// </summary>
        [Output("severity")]
        public Output<Pulumi.AwsNative.Redshift.EventSubscriptionSeverity?> Severity { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        /// </summary>
        [Output("snsTopicArn")]
        public Output<string?> SnsTopicArn { get; private set; } = null!;

        /// <summary>
        /// A list of one or more identifiers of Amazon Redshift source objects.
        /// </summary>
        [Output("sourceIds")]
        public Output<ImmutableArray<string>> SourceIds { get; private set; } = null!;

        /// <summary>
        /// A list of the sources that publish events to the Amazon Redshift event notification subscription.
        /// </summary>
        [Output("sourceIdsList")]
        public Output<ImmutableArray<string>> SourceIdsList { get; private set; } = null!;

        /// <summary>
        /// The type of source that will be generating the events.
        /// </summary>
        [Output("sourceType")]
        public Output<Pulumi.AwsNative.Redshift.EventSubscriptionSourceType?> SourceType { get; private set; } = null!;

        /// <summary>
        /// The status of the Amazon Redshift event notification subscription.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.Redshift.EventSubscriptionStatus> Status { get; private set; } = null!;

        /// <summary>
        /// The date and time the Amazon Redshift event notification subscription was created.
        /// </summary>
        [Output("subscriptionCreationTime")]
        public Output<string> SubscriptionCreationTime { get; private set; } = null!;

        /// <summary>
        /// The name of the Amazon Redshift event notification subscription
        /// </summary>
        [Output("subscriptionName")]
        public Output<string> SubscriptionName { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a EventSubscription resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EventSubscription(string name, EventSubscriptionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:redshift:EventSubscription", name, args ?? new EventSubscriptionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EventSubscription(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshift:EventSubscription", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "subscriptionName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing EventSubscription resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EventSubscription Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EventSubscription(name, id, options);
        }
    }

    public sealed class EventSubscriptionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("eventCategories")]
        private InputList<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem>? _eventCategories;

        /// <summary>
        /// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        /// </summary>
        public InputList<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem> EventCategories
        {
            get => _eventCategories ?? (_eventCategories = new InputList<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem>());
            set => _eventCategories = value;
        }

        /// <summary>
        /// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        /// </summary>
        [Input("severity")]
        public Input<Pulumi.AwsNative.Redshift.EventSubscriptionSeverity>? Severity { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        /// </summary>
        [Input("snsTopicArn")]
        public Input<string>? SnsTopicArn { get; set; }

        [Input("sourceIds")]
        private InputList<string>? _sourceIds;

        /// <summary>
        /// A list of one or more identifiers of Amazon Redshift source objects.
        /// </summary>
        public InputList<string> SourceIds
        {
            get => _sourceIds ?? (_sourceIds = new InputList<string>());
            set => _sourceIds = value;
        }

        /// <summary>
        /// The type of source that will be generating the events.
        /// </summary>
        [Input("sourceType")]
        public Input<Pulumi.AwsNative.Redshift.EventSubscriptionSourceType>? SourceType { get; set; }

        /// <summary>
        /// The name of the Amazon Redshift event notification subscription
        /// </summary>
        [Input("subscriptionName", required: true)]
        public Input<string> SubscriptionName { get; set; } = null!;

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

        public EventSubscriptionArgs()
        {
        }
        public static new EventSubscriptionArgs Empty => new EventSubscriptionArgs();
    }
}
