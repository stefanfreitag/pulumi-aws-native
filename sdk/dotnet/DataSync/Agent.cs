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
    /// Resource schema for AWS::DataSync::Agent.
    /// </summary>
    [AwsNativeResourceType("aws-native:datasync:Agent")]
    public partial class Agent : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Activation key of the Agent.
        /// </summary>
        [Output("activationKey")]
        public Output<string?> ActivationKey { get; private set; } = null!;

        /// <summary>
        /// The DataSync Agent ARN.
        /// </summary>
        [Output("agentArn")]
        public Output<string> AgentArn { get; private set; } = null!;

        /// <summary>
        /// The name configured for the agent. Text reference used to identify the agent in the console.
        /// </summary>
        [Output("agentName")]
        public Output<string?> AgentName { get; private set; } = null!;

        /// <summary>
        /// The service endpoints that the agent will connect to.
        /// </summary>
        [Output("endpointType")]
        public Output<Pulumi.AwsNative.DataSync.AgentEndpointType> EndpointType { get; private set; } = null!;

        /// <summary>
        /// The ARNs of the security group used to protect your data transfer task subnets.
        /// </summary>
        [Output("securityGroupArns")]
        public Output<ImmutableArray<string>> SecurityGroupArns { get; private set; } = null!;

        /// <summary>
        /// The ARNs of the subnets in which DataSync will create elastic network interfaces for each data transfer task.
        /// </summary>
        [Output("subnetArns")]
        public Output<ImmutableArray<string>> SubnetArns { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID of the VPC endpoint that the agent has access to.
        /// </summary>
        [Output("vpcEndpointId")]
        public Output<string?> VpcEndpointId { get; private set; } = null!;


        /// <summary>
        /// Create a Agent resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Agent(string name, AgentArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:datasync:Agent", name, args ?? new AgentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Agent(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:datasync:Agent", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "activationKey",
                    "securityGroupArns[*]",
                    "subnetArns[*]",
                    "vpcEndpointId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Agent resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Agent Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Agent(name, id, options);
        }
    }

    public sealed class AgentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Activation key of the Agent.
        /// </summary>
        [Input("activationKey")]
        public Input<string>? ActivationKey { get; set; }

        /// <summary>
        /// The name configured for the agent. Text reference used to identify the agent in the console.
        /// </summary>
        [Input("agentName")]
        public Input<string>? AgentName { get; set; }

        [Input("securityGroupArns")]
        private InputList<string>? _securityGroupArns;

        /// <summary>
        /// The ARNs of the security group used to protect your data transfer task subnets.
        /// </summary>
        public InputList<string> SecurityGroupArns
        {
            get => _securityGroupArns ?? (_securityGroupArns = new InputList<string>());
            set => _securityGroupArns = value;
        }

        [Input("subnetArns")]
        private InputList<string>? _subnetArns;

        /// <summary>
        /// The ARNs of the subnets in which DataSync will create elastic network interfaces for each data transfer task.
        /// </summary>
        public InputList<string> SubnetArns
        {
            get => _subnetArns ?? (_subnetArns = new InputList<string>());
            set => _subnetArns = value;
        }

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

        /// <summary>
        /// The ID of the VPC endpoint that the agent has access to.
        /// </summary>
        [Input("vpcEndpointId")]
        public Input<string>? VpcEndpointId { get; set; }

        public AgentArgs()
        {
        }
        public static new AgentArgs Empty => new AgentArgs();
    }
}
