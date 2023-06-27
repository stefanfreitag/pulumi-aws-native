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
    /// The resource schema for creating an Amazon Connect Customer Profiles Integration.
    /// </summary>
    [AwsNativeResourceType("aws-native:customerprofiles:Integration")]
    public partial class Integration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The time of this integration got created
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        [Output("flowDefinition")]
        public Output<Outputs.IntegrationFlowDefinition?> FlowDefinition { get; private set; } = null!;

        /// <summary>
        /// The time of this integration got last updated at
        /// </summary>
        [Output("lastUpdatedAt")]
        public Output<string> LastUpdatedAt { get; private set; } = null!;

        /// <summary>
        /// The name of the ObjectType defined for the 3rd party data in Profile Service
        /// </summary>
        [Output("objectTypeName")]
        public Output<string?> ObjectTypeName { get; private set; } = null!;

        /// <summary>
        /// The mapping between 3rd party event types and ObjectType names
        /// </summary>
        [Output("objectTypeNames")]
        public Output<ImmutableArray<Outputs.IntegrationObjectTypeMapping>> ObjectTypeNames { get; private set; } = null!;

        /// <summary>
        /// The tags (keys and values) associated with the integration
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.IntegrationTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The URI of the S3 bucket or any other type of data source.
        /// </summary>
        [Output("uri")]
        public Output<string?> Uri { get; private set; } = null!;


        /// <summary>
        /// Create a Integration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Integration(string name, IntegrationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:Integration", name, args ?? new IntegrationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Integration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:customerprofiles:Integration", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Integration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Integration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Integration(name, id, options);
        }
    }

    public sealed class IntegrationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique name of the domain.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        [Input("flowDefinition")]
        public Input<Inputs.IntegrationFlowDefinitionArgs>? FlowDefinition { get; set; }

        /// <summary>
        /// The name of the ObjectType defined for the 3rd party data in Profile Service
        /// </summary>
        [Input("objectTypeName")]
        public Input<string>? ObjectTypeName { get; set; }

        [Input("objectTypeNames")]
        private InputList<Inputs.IntegrationObjectTypeMappingArgs>? _objectTypeNames;

        /// <summary>
        /// The mapping between 3rd party event types and ObjectType names
        /// </summary>
        public InputList<Inputs.IntegrationObjectTypeMappingArgs> ObjectTypeNames
        {
            get => _objectTypeNames ?? (_objectTypeNames = new InputList<Inputs.IntegrationObjectTypeMappingArgs>());
            set => _objectTypeNames = value;
        }

        [Input("tags")]
        private InputList<Inputs.IntegrationTagArgs>? _tags;

        /// <summary>
        /// The tags (keys and values) associated with the integration
        /// </summary>
        public InputList<Inputs.IntegrationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.IntegrationTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The URI of the S3 bucket or any other type of data source.
        /// </summary>
        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public IntegrationArgs()
        {
        }
        public static new IntegrationArgs Empty => new IntegrationArgs();
    }
}
