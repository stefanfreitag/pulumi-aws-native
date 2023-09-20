// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lightsail::Container
 */
export class Container extends pulumi.CustomResource {
    /**
     * Get an existing Container resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Container {
        return new Container(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lightsail:Container';

    /**
     * Returns true if the given object is an instance of Container.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Container {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Container.__pulumiType;
    }

    public /*out*/ readonly containerArn!: pulumi.Output<string>;
    /**
     * Describes a container deployment configuration of an Amazon Lightsail container service.
     */
    public readonly containerServiceDeployment!: pulumi.Output<outputs.lightsail.ContainerServiceDeployment | undefined>;
    /**
     * A Boolean value to indicate whether the container service is disabled.
     */
    public readonly isDisabled!: pulumi.Output<boolean | undefined>;
    /**
     * The power specification for the container service.
     */
    public readonly power!: pulumi.Output<string>;
    /**
     * The principal ARN of the container service.
     */
    public /*out*/ readonly principalArn!: pulumi.Output<string>;
    /**
     * A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
     */
    public readonly privateRegistryAccess!: pulumi.Output<outputs.lightsail.ContainerPrivateRegistryAccess | undefined>;
    /**
     * The public domain names to use with the container service, such as example.com and www.example.com.
     */
    public readonly publicDomainNames!: pulumi.Output<outputs.lightsail.ContainerPublicDomainName[] | undefined>;
    /**
     * The scale specification for the container service.
     */
    public readonly scale!: pulumi.Output<number>;
    /**
     * The name for the container service.
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.lightsail.ContainerTag[] | undefined>;
    /**
     * The publicly accessible URL of the container service.
     */
    public /*out*/ readonly url!: pulumi.Output<string>;

    /**
     * Create a Container resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContainerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.power === undefined) && !opts.urn) {
                throw new Error("Missing required property 'power'");
            }
            if ((!args || args.scale === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scale'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["containerServiceDeployment"] = args ? args.containerServiceDeployment : undefined;
            resourceInputs["isDisabled"] = args ? args.isDisabled : undefined;
            resourceInputs["power"] = args ? args.power : undefined;
            resourceInputs["privateRegistryAccess"] = args ? args.privateRegistryAccess : undefined;
            resourceInputs["publicDomainNames"] = args ? args.publicDomainNames : undefined;
            resourceInputs["scale"] = args ? args.scale : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["containerArn"] = undefined /*out*/;
            resourceInputs["principalArn"] = undefined /*out*/;
            resourceInputs["url"] = undefined /*out*/;
        } else {
            resourceInputs["containerArn"] = undefined /*out*/;
            resourceInputs["containerServiceDeployment"] = undefined /*out*/;
            resourceInputs["isDisabled"] = undefined /*out*/;
            resourceInputs["power"] = undefined /*out*/;
            resourceInputs["principalArn"] = undefined /*out*/;
            resourceInputs["privateRegistryAccess"] = undefined /*out*/;
            resourceInputs["publicDomainNames"] = undefined /*out*/;
            resourceInputs["scale"] = undefined /*out*/;
            resourceInputs["serviceName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["url"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["serviceName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Container.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Container resource.
 */
export interface ContainerArgs {
    /**
     * Describes a container deployment configuration of an Amazon Lightsail container service.
     */
    containerServiceDeployment?: pulumi.Input<inputs.lightsail.ContainerServiceDeploymentArgs>;
    /**
     * A Boolean value to indicate whether the container service is disabled.
     */
    isDisabled?: pulumi.Input<boolean>;
    /**
     * The power specification for the container service.
     */
    power: pulumi.Input<string>;
    /**
     * A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
     */
    privateRegistryAccess?: pulumi.Input<inputs.lightsail.ContainerPrivateRegistryAccessArgs>;
    /**
     * The public domain names to use with the container service, such as example.com and www.example.com.
     */
    publicDomainNames?: pulumi.Input<pulumi.Input<inputs.lightsail.ContainerPublicDomainNameArgs>[]>;
    /**
     * The scale specification for the container service.
     */
    scale: pulumi.Input<number>;
    /**
     * The name for the container service.
     */
    serviceName: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.lightsail.ContainerTagArgs>[]>;
}
