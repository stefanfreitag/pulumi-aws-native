// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::DevEndpoint
 *
 * @deprecated DevEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class DevEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing DevEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DevEndpoint {
        pulumi.log.warn("DevEndpoint is deprecated: DevEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new DevEndpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:DevEndpoint';

    /**
     * Returns true if the given object is an instance of DevEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DevEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DevEndpoint.__pulumiType;
    }

    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DevEndpoint` for more information about the expected schema for this property.
     */
    public readonly arguments!: pulumi.Output<any | undefined>;
    public readonly endpointName!: pulumi.Output<string | undefined>;
    public readonly extraJarsS3Path!: pulumi.Output<string | undefined>;
    public readonly extraPythonLibsS3Path!: pulumi.Output<string | undefined>;
    public readonly glueVersion!: pulumi.Output<string | undefined>;
    public readonly numberOfNodes!: pulumi.Output<number | undefined>;
    public readonly numberOfWorkers!: pulumi.Output<number | undefined>;
    public readonly publicKey!: pulumi.Output<string | undefined>;
    public readonly publicKeys!: pulumi.Output<string[] | undefined>;
    public readonly roleArn!: pulumi.Output<string>;
    public readonly securityConfiguration!: pulumi.Output<string | undefined>;
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly subnetId!: pulumi.Output<string | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DevEndpoint` for more information about the expected schema for this property.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly workerType!: pulumi.Output<string | undefined>;

    /**
     * Create a DevEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated DevEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DevEndpointArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DevEndpoint is deprecated: DevEndpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            resourceInputs["arguments"] = args ? args.arguments : undefined;
            resourceInputs["endpointName"] = args ? args.endpointName : undefined;
            resourceInputs["extraJarsS3Path"] = args ? args.extraJarsS3Path : undefined;
            resourceInputs["extraPythonLibsS3Path"] = args ? args.extraPythonLibsS3Path : undefined;
            resourceInputs["glueVersion"] = args ? args.glueVersion : undefined;
            resourceInputs["numberOfNodes"] = args ? args.numberOfNodes : undefined;
            resourceInputs["numberOfWorkers"] = args ? args.numberOfWorkers : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["publicKeys"] = args ? args.publicKeys : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["securityConfiguration"] = args ? args.securityConfiguration : undefined;
            resourceInputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            resourceInputs["subnetId"] = args ? args.subnetId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["workerType"] = args ? args.workerType : undefined;
        } else {
            resourceInputs["arguments"] = undefined /*out*/;
            resourceInputs["endpointName"] = undefined /*out*/;
            resourceInputs["extraJarsS3Path"] = undefined /*out*/;
            resourceInputs["extraPythonLibsS3Path"] = undefined /*out*/;
            resourceInputs["glueVersion"] = undefined /*out*/;
            resourceInputs["numberOfNodes"] = undefined /*out*/;
            resourceInputs["numberOfWorkers"] = undefined /*out*/;
            resourceInputs["publicKey"] = undefined /*out*/;
            resourceInputs["publicKeys"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["securityConfiguration"] = undefined /*out*/;
            resourceInputs["securityGroupIds"] = undefined /*out*/;
            resourceInputs["subnetId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["workerType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["endpointName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DevEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DevEndpoint resource.
 */
export interface DevEndpointArgs {
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DevEndpoint` for more information about the expected schema for this property.
     */
    arguments?: any;
    endpointName?: pulumi.Input<string>;
    extraJarsS3Path?: pulumi.Input<string>;
    extraPythonLibsS3Path?: pulumi.Input<string>;
    glueVersion?: pulumi.Input<string>;
    numberOfNodes?: pulumi.Input<number>;
    numberOfWorkers?: pulumi.Input<number>;
    publicKey?: pulumi.Input<string>;
    publicKeys?: pulumi.Input<pulumi.Input<string>[]>;
    roleArn: pulumi.Input<string>;
    securityConfiguration?: pulumi.Input<string>;
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    subnetId?: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DevEndpoint` for more information about the expected schema for this property.
     */
    tags?: any;
    workerType?: pulumi.Input<string>;
}
