// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    /// <summary>
    /// Resource schema for AWS::DataSync::LocationAzureBlob.
    /// </summary>
    [AwsNativeResourceType("aws-native:datasync:LocationAzureBlob")]
    public partial class LocationAzureBlob : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.
        /// </summary>
        [Output("agentArns")]
        public Output<ImmutableArray<string>> AgentArns { get; private set; } = null!;

        /// <summary>
        /// Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.
        /// </summary>
        [Output("azureAccessTier")]
        public Output<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureAccessTier?> AzureAccessTier { get; private set; } = null!;

        /// <summary>
        /// The specific authentication type that you want DataSync to use to access your Azure Blob Container.
        /// </summary>
        [Output("azureBlobAuthenticationType")]
        public Output<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureBlobAuthenticationType> AzureBlobAuthenticationType { get; private set; } = null!;

        /// <summary>
        /// The URL of the Azure Blob container that was described.
        /// </summary>
        [Output("azureBlobContainerUrl")]
        public Output<string?> AzureBlobContainerUrl { get; private set; } = null!;

        [Output("azureBlobSasConfiguration")]
        public Output<Outputs.LocationAzureBlobAzureBlobSasConfiguration?> AzureBlobSasConfiguration { get; private set; } = null!;

        /// <summary>
        /// Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.
        /// </summary>
        [Output("azureBlobType")]
        public Output<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureBlobType?> AzureBlobType { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Azure Blob Location that is created.
        /// </summary>
        [Output("locationArn")]
        public Output<string> LocationArn { get; private set; } = null!;

        /// <summary>
        /// The URL of the Azure Blob Location that was described.
        /// </summary>
        [Output("locationUri")]
        public Output<string> LocationUri { get; private set; } = null!;

        /// <summary>
        /// The subdirectory in the Azure Blob Container that is used to read data from the Azure Blob Source Location.
        /// </summary>
        [Output("subdirectory")]
        public Output<string?> Subdirectory { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a LocationAzureBlob resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LocationAzureBlob(string name, LocationAzureBlobArgs args, CustomResourceOptions? options = null)
            : base("aws-native:datasync:LocationAzureBlob", name, args ?? new LocationAzureBlobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LocationAzureBlob(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:datasync:LocationAzureBlob", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "azureBlobContainerUrl",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LocationAzureBlob resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LocationAzureBlob Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new LocationAzureBlob(name, id, options);
        }
    }

    public sealed class LocationAzureBlobArgs : global::Pulumi.ResourceArgs
    {
        [Input("agentArns", required: true)]
        private InputList<string>? _agentArns;

        /// <summary>
        /// The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.
        /// </summary>
        public InputList<string> AgentArns
        {
            get => _agentArns ?? (_agentArns = new InputList<string>());
            set => _agentArns = value;
        }

        /// <summary>
        /// Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.
        /// </summary>
        [Input("azureAccessTier")]
        public Input<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureAccessTier>? AzureAccessTier { get; set; }

        /// <summary>
        /// The specific authentication type that you want DataSync to use to access your Azure Blob Container.
        /// </summary>
        [Input("azureBlobAuthenticationType", required: true)]
        public Input<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureBlobAuthenticationType> AzureBlobAuthenticationType { get; set; } = null!;

        /// <summary>
        /// The URL of the Azure Blob container that was described.
        /// </summary>
        [Input("azureBlobContainerUrl")]
        public Input<string>? AzureBlobContainerUrl { get; set; }

        [Input("azureBlobSasConfiguration")]
        public Input<Inputs.LocationAzureBlobAzureBlobSasConfigurationArgs>? AzureBlobSasConfiguration { get; set; }

        /// <summary>
        /// Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.
        /// </summary>
        [Input("azureBlobType")]
        public Input<Pulumi.AwsNative.DataSync.LocationAzureBlobAzureBlobType>? AzureBlobType { get; set; }

        /// <summary>
        /// The subdirectory in the Azure Blob Container that is used to read data from the Azure Blob Source Location.
        /// </summary>
        [Input("subdirectory")]
        public Input<string>? Subdirectory { get; set; }

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

        public LocationAzureBlobArgs()
        {
        }
        public static new LocationAzureBlobArgs Empty => new LocationAzureBlobArgs();
    }
}
