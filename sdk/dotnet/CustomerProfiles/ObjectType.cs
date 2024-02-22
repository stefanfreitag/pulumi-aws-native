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
    /// An ObjectType resource of Amazon Connect Customer Profiles
    /// </summary>
    [AwsNativeResourceType("aws-native:customerprofiles:ObjectType")]
    public partial class ObjectType : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates whether a profile should be created when data is received.
        /// </summary>
        [Output("allowProfileCreation")]
        public Output<bool?> AllowProfileCreation { get; private set; } = null!;

        /// <summary>
        /// The time of this integration got created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Description of the profile object type.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// The default encryption key
        /// </summary>
        [Output("encryptionKey")]
        public Output<string?> EncryptionKey { get; private set; } = null!;

        /// <summary>
        /// The default number of days until the data within the domain expires.
        /// </summary>
        [Output("expirationDays")]
        public Output<int?> ExpirationDays { get; private set; } = null!;

        /// <summary>
        /// A list of the name and ObjectType field.
        /// </summary>
        [Output("fields")]
        public Output<ImmutableArray<Outputs.ObjectTypeFieldMap>> Fields { get; private set; } = null!;

        /// <summary>
        /// A list of unique keys that can be used to map data to the profile.
        /// </summary>
        [Output("keys")]
        public Output<ImmutableArray<Outputs.ObjectTypeKeyMap>> Keys { get; private set; } = null!;

        /// <summary>
        /// The time of this integration got last updated at.
        /// </summary>
        [Output("lastUpdatedAt")]
        public Output<string> LastUpdatedAt { get; private set; } = null!;

        /// <summary>
        /// The name of the profile object type.
        /// </summary>
        [Output("objectTypeName")]
        public Output<string?> ObjectTypeName { get; private set; } = null!;

        /// <summary>
        /// The format of your sourceLastUpdatedTimestamp that was previously set up.
        /// </summary>
        [Output("sourceLastUpdatedTimestampFormat")]
        public Output<string?> SourceLastUpdatedTimestampFormat { get; private set; } = null!;

        /// <summary>
        /// The tags (keys and values) associated with the integration.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the object template.
        /// </summary>
        [Output("templateId")]
        public Output<string?> TemplateId { get; private set; } = null!;


        /// <summary>
        /// Create a ObjectType resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ObjectType(string name, ObjectTypeArgs args, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:ObjectType", name, args ?? new ObjectTypeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ObjectType(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:ObjectType", name, null, MakeResourceOptions(options, id))
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
                    "objectTypeName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ObjectType resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ObjectType Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ObjectType(name, id, options);
        }
    }

    public sealed class ObjectTypeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether a profile should be created when data is received.
        /// </summary>
        [Input("allowProfileCreation")]
        public Input<bool>? AllowProfileCreation { get; set; }

        /// <summary>
        /// Description of the profile object type.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        /// <summary>
        /// The default encryption key
        /// </summary>
        [Input("encryptionKey")]
        public Input<string>? EncryptionKey { get; set; }

        /// <summary>
        /// The default number of days until the data within the domain expires.
        /// </summary>
        [Input("expirationDays")]
        public Input<int>? ExpirationDays { get; set; }

        [Input("fields")]
        private InputList<Inputs.ObjectTypeFieldMapArgs>? _fields;

        /// <summary>
        /// A list of the name and ObjectType field.
        /// </summary>
        public InputList<Inputs.ObjectTypeFieldMapArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.ObjectTypeFieldMapArgs>());
            set => _fields = value;
        }

        [Input("keys")]
        private InputList<Inputs.ObjectTypeKeyMapArgs>? _keys;

        /// <summary>
        /// A list of unique keys that can be used to map data to the profile.
        /// </summary>
        public InputList<Inputs.ObjectTypeKeyMapArgs> Keys
        {
            get => _keys ?? (_keys = new InputList<Inputs.ObjectTypeKeyMapArgs>());
            set => _keys = value;
        }

        /// <summary>
        /// The name of the profile object type.
        /// </summary>
        [Input("objectTypeName")]
        public Input<string>? ObjectTypeName { get; set; }

        /// <summary>
        /// The format of your sourceLastUpdatedTimestamp that was previously set up.
        /// </summary>
        [Input("sourceLastUpdatedTimestampFormat")]
        public Input<string>? SourceLastUpdatedTimestampFormat { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags (keys and values) associated with the integration.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// A unique identifier for the object template.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        public ObjectTypeArgs()
        {
        }
        public static new ObjectTypeArgs Empty => new ObjectTypeArgs();
    }
}
