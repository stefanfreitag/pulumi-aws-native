// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SageMaker::CodeRepository
 *
 * @deprecated CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class CodeRepository extends pulumi.CustomResource {
    /**
     * Get an existing CodeRepository resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CodeRepository {
        pulumi.log.warn("CodeRepository is deprecated: CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new CodeRepository(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sagemaker:CodeRepository';

    /**
     * Returns true if the given object is an instance of CodeRepository.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CodeRepository {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CodeRepository.__pulumiType;
    }

    public readonly codeRepositoryName!: pulumi.Output<string | undefined>;
    public readonly gitConfig!: pulumi.Output<outputs.sagemaker.CodeRepositoryGitConfig>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a CodeRepository resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: CodeRepositoryArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("CodeRepository is deprecated: CodeRepository is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.gitConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gitConfig'");
            }
            resourceInputs["codeRepositoryName"] = args ? args.codeRepositoryName : undefined;
            resourceInputs["gitConfig"] = args ? args.gitConfig : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["codeRepositoryName"] = undefined /*out*/;
            resourceInputs["gitConfig"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["codeRepositoryName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CodeRepository.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CodeRepository resource.
 */
export interface CodeRepositoryArgs {
    codeRepositoryName?: pulumi.Input<string>;
    gitConfig: pulumi.Input<inputs.sagemaker.CodeRepositoryGitConfigArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
