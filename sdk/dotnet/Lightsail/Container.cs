// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::Container
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:Container")]
    public partial class Container : global::Pulumi.CustomResource
    {
        [Output("containerArn")]
        public Output<string> ContainerArn { get; private set; } = null!;

        /// <summary>
        /// Describes a container deployment configuration of an Amazon Lightsail container service.
        /// </summary>
        [Output("containerServiceDeployment")]
        public Output<Outputs.ContainerServiceDeployment?> ContainerServiceDeployment { get; private set; } = null!;

        /// <summary>
        /// A Boolean value to indicate whether the container service is disabled.
        /// </summary>
        [Output("isDisabled")]
        public Output<bool?> IsDisabled { get; private set; } = null!;

        /// <summary>
        /// The power specification for the container service.
        /// </summary>
        [Output("power")]
        public Output<string> Power { get; private set; } = null!;

        /// <summary>
        /// The principal ARN of the container service.
        /// </summary>
        [Output("principalArn")]
        public Output<string> PrincipalArn { get; private set; } = null!;

        /// <summary>
        /// A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
        /// </summary>
        [Output("privateRegistryAccess")]
        public Output<Outputs.ContainerPrivateRegistryAccess?> PrivateRegistryAccess { get; private set; } = null!;

        /// <summary>
        /// The public domain names to use with the container service, such as example.com and www.example.com.
        /// </summary>
        [Output("publicDomainNames")]
        public Output<ImmutableArray<Outputs.ContainerPublicDomainName>> PublicDomainNames { get; private set; } = null!;

        /// <summary>
        /// The scale specification for the container service.
        /// </summary>
        [Output("scale")]
        public Output<int> Scale { get; private set; } = null!;

        /// <summary>
        /// The name for the container service.
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ContainerTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The publicly accessible URL of the container service.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a Container resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Container(string name, ContainerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Container", name, args ?? new ContainerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Container(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Container", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "serviceName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Container resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Container Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Container(name, id, options);
        }
    }

    public sealed class ContainerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Describes a container deployment configuration of an Amazon Lightsail container service.
        /// </summary>
        [Input("containerServiceDeployment")]
        public Input<Inputs.ContainerServiceDeploymentArgs>? ContainerServiceDeployment { get; set; }

        /// <summary>
        /// A Boolean value to indicate whether the container service is disabled.
        /// </summary>
        [Input("isDisabled")]
        public Input<bool>? IsDisabled { get; set; }

        /// <summary>
        /// The power specification for the container service.
        /// </summary>
        [Input("power", required: true)]
        public Input<string> Power { get; set; } = null!;

        /// <summary>
        /// A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
        /// </summary>
        [Input("privateRegistryAccess")]
        public Input<Inputs.ContainerPrivateRegistryAccessArgs>? PrivateRegistryAccess { get; set; }

        [Input("publicDomainNames")]
        private InputList<Inputs.ContainerPublicDomainNameArgs>? _publicDomainNames;

        /// <summary>
        /// The public domain names to use with the container service, such as example.com and www.example.com.
        /// </summary>
        public InputList<Inputs.ContainerPublicDomainNameArgs> PublicDomainNames
        {
            get => _publicDomainNames ?? (_publicDomainNames = new InputList<Inputs.ContainerPublicDomainNameArgs>());
            set => _publicDomainNames = value;
        }

        /// <summary>
        /// The scale specification for the container service.
        /// </summary>
        [Input("scale", required: true)]
        public Input<int> Scale { get; set; } = null!;

        /// <summary>
        /// The name for the container service.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ContainerTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ContainerTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ContainerTagArgs>());
            set => _tags = value;
        }

        public ContainerArgs()
        {
        }
        public static new ContainerArgs Empty => new ContainerArgs();
    }
}
