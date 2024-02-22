// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles
{
    /// <summary>
    /// A domain defined for 3rd party data source in Profile Service
    /// </summary>
    [AwsNativeResourceType("aws-native:customerprofiles:Domain")]
    public partial class Domain : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The time of this integration got created
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The URL of the SQS dead letter queue
        /// </summary>
        [Output("deadLetterQueueUrl")]
        public Output<string?> DeadLetterQueueUrl { get; private set; } = null!;

        /// <summary>
        /// The default encryption key
        /// </summary>
        [Output("defaultEncryptionKey")]
        public Output<string?> DefaultEncryptionKey { get; private set; } = null!;

        /// <summary>
        /// The default number of days until the data within the domain expires.
        /// </summary>
        [Output("defaultExpirationDays")]
        public Output<int?> DefaultExpirationDays { get; private set; } = null!;

        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// The time of this integration got last updated at
        /// </summary>
        [Output("lastUpdatedAt")]
        public Output<string> LastUpdatedAt { get; private set; } = null!;

        [Output("matching")]
        public Output<Outputs.DomainMatching?> Matching { get; private set; } = null!;

        [Output("ruleBasedMatching")]
        public Output<Outputs.DomainRuleBasedMatching?> RuleBasedMatching { get; private set; } = null!;

        [Output("stats")]
        public Output<Outputs.DomainStats> Stats { get; private set; } = null!;

        /// <summary>
        /// The tags (keys and values) associated with the domain
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:Domain", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "domainName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, options);
        }
    }

    public sealed class DomainArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The URL of the SQS dead letter queue
        /// </summary>
        [Input("deadLetterQueueUrl")]
        public Input<string>? DeadLetterQueueUrl { get; set; }

        /// <summary>
        /// The default encryption key
        /// </summary>
        [Input("defaultEncryptionKey")]
        public Input<string>? DefaultEncryptionKey { get; set; }

        /// <summary>
        /// The default number of days until the data within the domain expires.
        /// </summary>
        [Input("defaultExpirationDays")]
        public Input<int>? DefaultExpirationDays { get; set; }

        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        [Input("matching")]
        public Input<Inputs.DomainMatchingArgs>? Matching { get; set; }

        [Input("ruleBasedMatching")]
        public Input<Inputs.DomainRuleBasedMatchingArgs>? RuleBasedMatching { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags (keys and values) associated with the domain
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public DomainArgs()
        {
        }
        public static new DomainArgs Empty => new DomainArgs();
    }
}
