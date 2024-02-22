// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchServerless
{
    /// <summary>
    /// Amazon OpenSearchServerless collection resource
    /// </summary>
    [AwsNativeResourceType("aws-native:opensearchserverless:Collection")]
    public partial class Collection : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the collection.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The endpoint for the collection.
        /// </summary>
        [Output("collectionEndpoint")]
        public Output<string> CollectionEndpoint { get; private set; } = null!;

        /// <summary>
        /// The OpenSearch Dashboards endpoint for the collection.
        /// </summary>
        [Output("dashboardEndpoint")]
        public Output<string> DashboardEndpoint { get; private set; } = null!;

        /// <summary>
        /// The description of the collection
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the collection.
        /// 
        /// The name must meet the following criteria:
        /// Unique to your account and AWS Region
        /// Starts with a lowercase letter
        /// Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
        /// Contains between 3 and 32 characters
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("standbyReplicas")]
        public Output<Pulumi.AwsNative.OpenSearchServerless.CollectionStandbyReplicas?> StandbyReplicas { get; private set; } = null!;

        /// <summary>
        /// List of tags to be added to the resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.CreateOnlyTag>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.OpenSearchServerless.CollectionType?> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Collection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Collection(string name, CollectionArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:opensearchserverless:Collection", name, args ?? new CollectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Collection(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:opensearchserverless:Collection", name, null, MakeResourceOptions(options, id))
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
                    "tags[*]",
                    "type",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Collection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Collection Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Collection(name, id, options);
        }
    }

    public sealed class CollectionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the collection
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the collection.
        /// 
        /// The name must meet the following criteria:
        /// Unique to your account and AWS Region
        /// Starts with a lowercase letter
        /// Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)
        /// Contains between 3 and 32 characters
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("standbyReplicas")]
        public Input<Pulumi.AwsNative.OpenSearchServerless.CollectionStandbyReplicas>? StandbyReplicas { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>? _tags;

        /// <summary>
        /// List of tags to be added to the resource
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>());
            set => _tags = value;
        }

        [Input("type")]
        public Input<Pulumi.AwsNative.OpenSearchServerless.CollectionType>? Type { get; set; }

        public CollectionArgs()
        {
        }
        public static new CollectionArgs Empty => new CollectionArgs();
    }
}
