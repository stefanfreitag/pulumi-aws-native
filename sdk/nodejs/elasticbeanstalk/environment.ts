// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticBeanstalk::Environment
 *
 * @deprecated Environment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Environment extends pulumi.CustomResource {
    /**
     * Get an existing Environment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Environment {
        pulumi.log.warn("Environment is deprecated: Environment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Environment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticbeanstalk:Environment';

    /**
     * Returns true if the given object is an instance of Environment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Environment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Environment.__pulumiType;
    }

    public readonly applicationName!: pulumi.Output<string>;
    public readonly cNAMEPrefix!: pulumi.Output<string | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly endpointURL!: pulumi.Output<string>;
    public readonly environmentName!: pulumi.Output<string | undefined>;
    public readonly operationsRole!: pulumi.Output<string | undefined>;
    public readonly optionSettings!: pulumi.Output<outputs.elasticbeanstalk.EnvironmentOptionSetting[] | undefined>;
    public readonly platformArn!: pulumi.Output<string | undefined>;
    public readonly solutionStackName!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.elasticbeanstalk.EnvironmentTag[] | undefined>;
    public readonly templateName!: pulumi.Output<string | undefined>;
    public readonly tier!: pulumi.Output<outputs.elasticbeanstalk.EnvironmentTier | undefined>;
    public readonly versionLabel!: pulumi.Output<string | undefined>;

    /**
     * Create a Environment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Environment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: EnvironmentArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Environment is deprecated: Environment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationName'");
            }
            inputs["applicationName"] = args ? args.applicationName : undefined;
            inputs["cNAMEPrefix"] = args ? args.cNAMEPrefix : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["environmentName"] = args ? args.environmentName : undefined;
            inputs["operationsRole"] = args ? args.operationsRole : undefined;
            inputs["optionSettings"] = args ? args.optionSettings : undefined;
            inputs["platformArn"] = args ? args.platformArn : undefined;
            inputs["solutionStackName"] = args ? args.solutionStackName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["templateName"] = args ? args.templateName : undefined;
            inputs["tier"] = args ? args.tier : undefined;
            inputs["versionLabel"] = args ? args.versionLabel : undefined;
            inputs["endpointURL"] = undefined /*out*/;
        } else {
            inputs["applicationName"] = undefined /*out*/;
            inputs["cNAMEPrefix"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["endpointURL"] = undefined /*out*/;
            inputs["environmentName"] = undefined /*out*/;
            inputs["operationsRole"] = undefined /*out*/;
            inputs["optionSettings"] = undefined /*out*/;
            inputs["platformArn"] = undefined /*out*/;
            inputs["solutionStackName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["templateName"] = undefined /*out*/;
            inputs["tier"] = undefined /*out*/;
            inputs["versionLabel"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Environment.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Environment resource.
 */
export interface EnvironmentArgs {
    applicationName: pulumi.Input<string>;
    cNAMEPrefix?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    environmentName?: pulumi.Input<string>;
    operationsRole?: pulumi.Input<string>;
    optionSettings?: pulumi.Input<pulumi.Input<inputs.elasticbeanstalk.EnvironmentOptionSettingArgs>[]>;
    platformArn?: pulumi.Input<string>;
    solutionStackName?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.elasticbeanstalk.EnvironmentTagArgs>[]>;
    templateName?: pulumi.Input<string>;
    tier?: pulumi.Input<inputs.elasticbeanstalk.EnvironmentTierArgs>;
    versionLabel?: pulumi.Input<string>;
}
