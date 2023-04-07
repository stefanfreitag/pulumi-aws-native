// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AmazonMQ::Configuration
 *
 * @deprecated Configuration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Configuration extends pulumi.CustomResource {
    /**
     * Get an existing Configuration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Configuration {
        pulumi.log.warn("Configuration is deprecated: Configuration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Configuration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:amazonmq:Configuration';

    /**
     * Returns true if the given object is an instance of Configuration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Configuration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Configuration.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly authenticationStrategy!: pulumi.Output<string | undefined>;
    public readonly data!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly engineType!: pulumi.Output<string>;
    public readonly engineVersion!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly revision!: pulumi.Output<number>;
    public readonly tags!: pulumi.Output<outputs.amazonmq.ConfigurationTagsEntry[] | undefined>;

    /**
     * Create a Configuration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Configuration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Configuration is deprecated: Configuration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.data === undefined) && !opts.urn) {
                throw new Error("Missing required property 'data'");
            }
            if ((!args || args.engineType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineType'");
            }
            if ((!args || args.engineVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineVersion'");
            }
            resourceInputs["authenticationStrategy"] = args ? args.authenticationStrategy : undefined;
            resourceInputs["data"] = args ? args.data : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["engineType"] = args ? args.engineType : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["revision"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["authenticationStrategy"] = undefined /*out*/;
            resourceInputs["data"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["engineType"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["revision"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Configuration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Configuration resource.
 */
export interface ConfigurationArgs {
    authenticationStrategy?: pulumi.Input<string>;
    data: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    engineType: pulumi.Input<string>;
    engineVersion: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.amazonmq.ConfigurationTagsEntryArgs>[]>;
}
